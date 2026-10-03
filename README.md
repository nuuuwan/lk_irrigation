# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_06:31:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,501 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 06:31:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.001 |  |
| 2026-10-03 06:27:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-03 06:13:15 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-03 06:13:14 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-03 06:10:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.114 |  |
| 2026-10-03 06:08:43 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.007 |  |
| 2026-10-03 06:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 06:07:09 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.046 |  |
| 2026-10-03 06:06:54 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:06:51 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 06:05:55 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.074 |  |
| 2026-10-03 06:04:54 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.201 |  |
| 2026-10-03 06:04:46 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 06:04:36 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 06:04:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:04:07 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-10-03 06:03:58 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:03:25 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-10-03 06:03:04 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 06:03:01 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 06:02:54 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.051 |  |
| 2026-10-03 06:02:52 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.058 |  |
| 2026-10-03 06:02:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:41 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.020 |  |
| 2026-10-03 06:02:31 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.194 |  |
| 2026-10-03 06:02:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.071 |  |
| 2026-10-03 06:02:25 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-03 06:02:20 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 06:02:01 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:32 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:28 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.033 |  |
| 2026-10-03 06:01:22 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:04 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-03 06:00:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-10-03 06:00:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 06:06:51 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 06:27:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-03 06:13:14 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-03 06:02:20 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 06:03:01 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 06:13:15 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-03 06:01:04 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-03 06:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 06:04:36 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 06:04:46 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 06:03:04 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 06:31:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.001 |  |
| 2026-10-03 06:02:52 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:25 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:06:54 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:01 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:04:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:02:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:03:58 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:32 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:01:22 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 06:08:43 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.007 |  |
| 2026-10-03 06:02:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-03 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-10-03 06:02:41 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.020 |  |
| 2026-10-03 06:04:07 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-10-03 06:01:28 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.033 |  |
| 2026-10-03 06:07:09 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.046 |  |
| 2026-10-03 06:02:54 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.051 |  |
| 2026-10-03 06:03:25 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-10-03 06:00:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-10-03 06:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.058 |  |
| 2026-10-03 06:02:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.071 |  |
| 2026-10-03 06:05:55 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.074 |  |
| 2026-10-03 06:10:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.114 |  |
| 2026-10-03 06:02:31 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.194 |  |
| 2026-10-03 06:04:54 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)