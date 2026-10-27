# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_14:18:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 14:18:38 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:11:29 | Rathnapura (Kalu Ganga) | 8.17 | 🟠 Minor Flood | -0.082 |  |
| 2026-10-27 14:08:52 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.096 |  |
| 2026-10-27 14:08:06 | Galgamuwa (Mee Oya) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:06:36 | Badalgama (Maha Oya) | 4.65 | 🟢 Normal | -0.140 |  |
| 2026-10-27 14:05:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 14:05:24 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-10-27 14:05:12 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.145 |  |
| 2026-10-27 14:05:04 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 14:04:55 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-10-27 14:04:17 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.263 |  |
| 2026-10-27 14:04:13 | Peradeniya (Mahaweli Ganga) | 3.41 | 🟢 Normal | -0.062 |  |
| 2026-10-27 14:04:12 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.049 |  |
| 2026-10-27 14:03:54 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.096 |  |
| 2026-10-27 14:03:47 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:03:26 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | -0.042 |  |
| 2026-10-27 14:03:22 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 14:03:17 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 14:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.55 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 14:03:10 | Ellagawa (Kalu Ganga) | 10.03 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 14:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-27 14:03:01 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:02:37 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-27 14:02:31 | Thanthirimale (Malwathu Oya) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-10-27 14:02:23 | Putupaula (Kalu Ganga) | 3.33 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 14:02:16 | Hanwella (Kelani Ganga) | 5.87 | 🟢 Normal | -0.131 |  |
| 2026-10-27 14:02:15 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:02:13 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-27 14:02:13 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:02:11 | Moragaswewa (Deduru Oya) | 5.10 | 🟡 Alert | -0.060 |  |
| 2026-10-27 14:01:59 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-27 14:01:51 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 14:01:44 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.149 |  |
| 2026-10-27 14:01:19 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.001 |  |
| 2026-10-27 14:01:06 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:01:03 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:00:44 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.063 |  |
| 2026-10-27 14:00:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:59:39 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 14:04:55 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-10-27 14:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.55 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 14:01:51 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 14:05:04 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 14:11:29 | Rathnapura (Kalu Ganga) | 8.17 | 🟠 Minor Flood | -0.082 |  |
| 2026-10-27 14:02:23 | Putupaula (Kalu Ganga) | 3.33 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 14:03:10 | Ellagawa (Kalu Ganga) | 10.03 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 14:03:17 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 14:02:11 | Moragaswewa (Deduru Oya) | 5.10 | 🟡 Alert | -0.060 |  |
| 2026-10-27 14:00:44 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.063 |  |
| 2026-10-27 14:01:59 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-27 14:02:37 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-27 14:03:22 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 14:05:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 14:01:19 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.001 |  |
| 2026-10-27 14:02:15 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:03:47 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:08:06 | Galgamuwa (Mee Oya) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:02:13 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:18:38 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:01:03 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:03:01 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:01:06 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-27 14:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-27 14:02:13 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-27 14:00:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-27 14:05:24 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-10-27 14:02:31 | Thanthirimale (Malwathu Oya) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-10-27 14:03:26 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | -0.042 |  |
| 2026-10-27 14:04:12 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.049 |  |
| 2026-10-27 14:04:13 | Peradeniya (Mahaweli Ganga) | 3.41 | 🟢 Normal | -0.062 |  |
| 2026-10-27 13:59:39 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | -0.091 |  |
| 2026-10-27 14:08:52 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.096 |  |
| 2026-10-27 14:03:54 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.096 |  |
| 2026-10-27 14:02:16 | Hanwella (Kelani Ganga) | 5.87 | 🟢 Normal | -0.131 |  |
| 2026-10-27 14:06:36 | Badalgama (Maha Oya) | 4.65 | 🟢 Normal | -0.140 |  |
| 2026-10-27 14:05:12 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.145 |  |
| 2026-10-27 14:01:44 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.149 |  |
| 2026-10-27 14:04:17 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.263 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)