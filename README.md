# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_18:27:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 18:27:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:15:26 | Urawa (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.082 |  |
| 2026-09-24 18:10:27 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.175 |  |
| 2026-09-24 18:08:48 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-24 18:07:43 | Panadugama (Nilwala Ganga) | 6.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 18:07:41 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-24 18:05:47 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-24 18:05:17 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-24 18:05:12 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:39 | Rathnapura (Kalu Ganga) | 5.93 | 🟡 Alert | -0.019 |  |
| 2026-09-24 18:04:32 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 18:04:09 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 18:04:05 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-09-24 18:04:00 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 18:03:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-24 18:03:55 | Glencourse (Kelani Ganga) | 13.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 18:03:39 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:33 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:23 | Baddegama (Gin Ganga) | 4.45 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 18:03:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:13 | Deraniyagala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.536 | 🔺 Rising |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-09-24 18:02:54 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-24 18:02:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-09-24 18:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 18:02:40 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:31 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-24 18:02:28 | Thawalama (Gin Ganga) | 5.23 | 🟡 Alert | -0.043 |  |
| 2026-09-24 18:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:18 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 18:01:49 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-24 18:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:12 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:00:31 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:00:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 18:03:23 | Baddegama (Gin Ganga) | 4.45 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 18:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 18:07:43 | Panadugama (Nilwala Ganga) | 6.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 18:04:32 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 18:02:18 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 18:04:39 | Rathnapura (Kalu Ganga) | 5.93 | 🟡 Alert | -0.019 |  |
| 2026-09-24 18:02:28 | Thawalama (Gin Ganga) | 5.23 | 🟡 Alert | -0.043 |  |
| 2026-09-24 18:03:13 | Deraniyagala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.536 | 🔺 Rising |
| 2026-09-24 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-09-24 18:05:12 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-24 18:08:48 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-24 18:05:17 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-24 18:02:31 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-24 18:04:09 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 18:02:54 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-24 18:03:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-24 18:04:00 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 18:03:55 | Glencourse (Kelani Ganga) | 13.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 18:07:41 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-24 18:05:47 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:00:31 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:00:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:33 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:27:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:03:39 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:12 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:49 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:40 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:01:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-24 18:04:05 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-09-24 18:02:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-09-24 18:15:26 | Urawa (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.082 |  |
| 2026-09-24 18:10:27 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)