# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_11:15:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,827 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 11:15:05 | Galgamuwa (Mee Oya) | 2.25 | 🟢 Normal | -0.008 |  |
| 2026-10-22 11:14:44 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 11:09:49 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:08:10 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.049 |  |
| 2026-10-22 11:07:57 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-22 11:07:48 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-22 11:07:38 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.065 |  |
| 2026-10-22 11:07:38 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.047 |  |
| 2026-10-22 11:07:15 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:06:54 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.190 |  |
| 2026-10-22 11:06:31 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:06:31 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-22 11:06:23 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-22 11:05:29 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-22 11:05:25 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.026 |  |
| 2026-10-22 11:05:19 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:04:35 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-10-22 11:04:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-22 11:04:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 11:04:10 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.077 |  |
| 2026-10-22 11:03:40 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -1.628 |  |
| 2026-10-22 11:03:33 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:03:31 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-10-22 11:03:30 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.051 |  |
| 2026-10-22 11:03:15 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-10-22 11:02:50 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-22 11:02:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 11:02:36 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-10-22 11:02:29 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-22 11:02:09 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.163 |  |
| 2026-10-22 11:02:03 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.012 |  |
| 2026-10-22 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-22 11:01:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:01:07 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-22 11:00:51 | Thanthirimale (Malwathu Oya) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 11:00:29 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:00:26 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-10-22 11:00:22 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.324 |  |
| 2026-10-22 11:00:14 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-22 11:06:23 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-22 11:05:29 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-22 11:06:31 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-22 11:07:48 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-22 11:01:07 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-22 11:07:57 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-22 11:04:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-22 11:04:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 11:14:44 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 11:00:51 | Thanthirimale (Malwathu Oya) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 11:02:03 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:00:29 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:09:49 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:05:19 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:01:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:07:15 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:06:31 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-22 11:15:05 | Galgamuwa (Mee Oya) | 2.25 | 🟢 Normal | -0.008 |  |
| 2026-10-22 11:02:29 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-22 11:02:50 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-22 11:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.012 |  |
| 2026-10-22 11:03:31 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-10-22 11:02:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 11:05:25 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.026 |  |
| 2026-10-22 11:00:26 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-10-22 11:02:36 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-10-22 11:03:15 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-10-22 11:07:38 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.047 |  |
| 2026-10-22 11:08:10 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.049 |  |
| 2026-10-22 11:03:30 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.051 |  |
| 2026-10-22 11:04:35 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-10-22 11:00:14 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.065 |  |
| 2026-10-22 11:07:38 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.065 |  |
| 2026-10-22 11:04:10 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.077 |  |
| 2026-10-22 11:02:09 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.163 |  |
| 2026-10-22 11:06:54 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.190 |  |
| 2026-10-22 11:00:22 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.324 |  |
| 2026-10-22 11:03:40 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -1.628 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)