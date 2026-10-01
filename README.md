# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_12:13:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,945 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 12:13:58 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:10:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:09:17 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:08:22 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:06:25 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:06:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:05:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:05:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 12:05:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-01 12:04:39 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-01 12:04:29 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:04:19 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:04:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:04:12 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:04:11 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.019 |  |
| 2026-10-01 12:03:48 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:39 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:39 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:30 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.043 |  |
| 2026-10-01 12:03:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:03:17 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:03:14 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.158 |  |
| 2026-10-01 12:03:13 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-01 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-01 12:02:50 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:37 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:33 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:30 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.020 |  |
| 2026-10-01 12:02:13 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:10 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:08 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.007 |  |
| 2026-10-01 12:02:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:01:38 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:01:24 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:01:17 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:00:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.041 |  |
| 2026-10-01 12:00:49 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:00:27 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:59:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 12:05:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-01 12:05:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 12:02:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:00:49 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:06:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:04:12 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:13:58 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:04:19 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:03:17 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:09:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:03:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:50 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:05:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:10:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:01:38 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:08 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.007 |  |
| 2026-10-01 12:08:22 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:37 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:33 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:04:29 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:10 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:01:17 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:04:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:02:13 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:01:24 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:09:17 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:39 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:48 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:03:39 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.010 |  |
| 2026-10-01 12:04:11 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.019 |  |
| 2026-10-01 12:03:13 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-01 12:02:30 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.020 |  |
| 2026-10-01 12:04:39 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-01 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-01 12:00:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.041 |  |
| 2026-10-01 12:03:30 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.043 |  |
| 2026-10-01 12:03:14 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)