# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_00:12:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 00:12:50 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.017 |  |
| 2026-10-05 00:12:45 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-05 00:11:28 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.261 |  |
| 2026-10-05 00:09:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:09:37 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-05 00:08:19 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-10-05 00:08:13 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-05 00:06:13 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-05 00:06:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:05:16 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 00:05:15 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-05 00:04:52 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-10-05 00:04:31 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-05 00:04:05 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.098 |  |
| 2026-10-05 00:03:49 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-10-05 00:03:47 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 00:03:46 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:03:22 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |
| 2026-10-05 00:03:12 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-05 00:03:08 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 00:02:48 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:38 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:11 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-05 00:01:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:01:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-10-05 00:01:30 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.072 |  |
| 2026-10-05 00:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-10-05 00:00:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:00:10 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 22:09:19 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 19.565 | 🔺 Rising |
| 2026-10-05 00:03:49 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-10-05 00:05:15 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-05 00:12:45 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-05 00:08:13 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-04 23:02:35 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-05 00:03:12 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-05 00:06:13 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-05 00:03:47 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 00:09:37 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-05 00:03:08 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 00:05:16 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 00:00:10 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 00:03:46 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:38 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:01:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:48 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:08:01 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-04 23:15:27 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:06:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:00:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:09:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:11 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 00:12:50 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.017 |  |
| 2026-10-04 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2026-10-05 00:04:52 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-10-05 00:04:31 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-05 00:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-10-05 00:08:19 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-10-05 00:01:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-10-05 00:01:30 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.072 |  |
| 2026-10-05 00:03:22 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |
| 2026-10-05 00:04:05 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.098 |  |
| 2026-10-05 00:11:28 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.261 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)