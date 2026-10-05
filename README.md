# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_06:31:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 06:31:47 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:29:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.004 |  |
| 2026-10-05 06:13:53 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-10-05 06:12:21 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.036 |  |
| 2026-10-05 06:08:28 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.020 |  |
| 2026-10-05 06:07:28 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.046 |  |
| 2026-10-05 06:07:24 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:06:58 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.036 |  |
| 2026-10-05 06:06:54 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 06:05:58 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.038 |  |
| 2026-10-05 06:05:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 06:05:12 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:04:52 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-10-05 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.078 |  |
| 2026-10-05 06:04:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:04:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.038 |  |
| 2026-10-05 06:03:50 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:03:26 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 06:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | 1.983 | 🔺 Rising |
| 2026-10-05 06:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-05 06:05:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 06:01:41 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-05 06:01:19 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 06:06:54 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 06:29:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.004 |  |
| 2026-10-05 06:05:12 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:01:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:03:50 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:02:10 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:01:42 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:02:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:31:47 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:04:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:03:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:07:24 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:01:17 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:01:03 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-05 06:02:48 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-05 06:08:28 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.020 |  |
| 2026-10-05 06:03:07 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2026-10-05 06:01:31 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.024 |  |
| 2026-10-05 06:04:52 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-10-05 06:13:53 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-10-05 06:12:21 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.036 |  |
| 2026-10-05 06:06:58 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.036 |  |
| 2026-10-05 06:05:58 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.038 |  |
| 2026-10-05 06:04:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.038 |  |
| 2026-10-05 06:02:32 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-10-05 06:07:28 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.046 |  |
| 2026-10-05 06:02:20 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-10-05 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-10-05 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.069 |  |
| 2026-10-05 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.078 |  |
| 2026-10-05 06:03:13 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.184 |  |
| 2026-10-05 06:02:42 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.185 |  |
| 2026-10-05 06:00:50 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)