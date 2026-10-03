# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_03:19:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,301 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 03:19:06 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.079 |  |
| 2026-10-04 03:16:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 03:15:59 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -6.353 |  |
| 2026-10-04 03:15:42 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -6.353 |  |
| 2026-10-04 03:10:38 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.009 |  |
| 2026-10-04 03:09:56 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.048 |  |
| 2026-10-04 03:09:19 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:07:49 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-04 03:07:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:07:06 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.027 |  |
| 2026-10-04 03:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -1.800 |  |
| 2026-10-04 03:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -1.800 |  |
| 2026-10-04 03:05:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -1.800 |  |
| 2026-10-04 03:05:02 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.336 |  |
| 2026-10-04 03:03:56 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:49 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:03:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-04 03:03:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:15 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-04 03:03:14 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:12 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:09 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-04 03:03:03 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:02:40 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-04 03:02:30 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:02:11 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.207 |  |
| 2026-10-04 03:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:02:03 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:02:00 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.100 |  |
| 2026-10-04 03:01:59 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.161 |  |
| 2026-10-04 03:01:53 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:01:22 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:00:16 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 03:03:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-04 03:03:15 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-04 03:07:49 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-04 03:16:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 01:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 03:05:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:02:30 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:01:53 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:01:22 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:02:29 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:00:16 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:02:03 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:09:19 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:56 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:41:02 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:43 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:03:14 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 03:10:38 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.009 |  |
| 2026-10-04 03:03:03 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:03:49 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:07:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-04 03:02:40 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-04 03:03:09 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-04 03:07:06 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.027 |  |
| 2026-10-04 03:09:56 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.048 |  |
| 2026-10-04 03:19:06 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.079 |  |
| 2026-10-04 03:02:00 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.100 |  |
| 2026-10-04 03:01:59 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.161 |  |
| 2026-10-04 03:02:11 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.207 |  |
| 2026-10-04 03:05:02 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.336 |  |
| 2026-10-04 03:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -1.800 |  |
| 2026-10-04 03:15:59 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -6.353 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)