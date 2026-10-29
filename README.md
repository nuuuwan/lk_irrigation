# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_07:04:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,948 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 07:04:01 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.047 |  |
| 2026-10-29 07:04:00 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-29 07:03:58 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.072 |  |
| 2026-10-29 07:03:38 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:35 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | -0.010 |  |
| 2026-10-29 07:03:31 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-10-29 07:03:19 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.060 |  |
| 2026-10-29 07:03:14 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 07:03:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:02:48 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.087 |  |
| 2026-10-29 07:02:42 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 07:02:39 | Ellagawa (Kalu Ganga) | 10.12 | 🟡 Alert | -0.052 |  |
| 2026-10-29 07:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-10-29 07:02:12 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-29 07:02:07 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:01:57 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:01:29 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.051 |  |
| 2026-10-29 07:01:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:01:05 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-10-29 07:01:02 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 07:00:14 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.061 |  |
| 2026-10-29 07:00:09 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:00:08 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-10-29 06:36:00 | Galgamuwa (Mee Oya) | 1.94 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 06:02:20 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 06:03:33 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 06:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.038 |  |
| 2026-10-29 06:06:45 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-10-29 07:03:35 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | -0.010 |  |
| 2026-10-29 07:02:39 | Ellagawa (Kalu Ganga) | 10.12 | 🟡 Alert | -0.052 |  |
| 2026-10-29 07:01:02 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 07:03:14 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 06:06:10 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-29 07:02:42 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 07:00:09 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:01:57 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:38 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:01:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:16:02 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:07:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:02:07 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:31 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-10-29 07:04:00 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-29 07:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-10-29 06:06:33 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 07:02:12 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-29 06:06:41 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:01:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-10-29 06:36:00 | Galgamuwa (Mee Oya) | 1.94 | 🟢 Normal | -0.034 |  |
| 2026-10-29 07:04:01 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.047 |  |
| 2026-10-29 07:01:05 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-10-29 07:01:29 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.051 |  |
| 2026-10-29 07:00:08 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-10-29 07:03:19 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.060 |  |
| 2026-10-29 07:00:14 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.061 |  |
| 2026-10-29 07:03:58 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.072 |  |
| 2026-10-29 06:11:16 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.073 |  |
| 2026-10-29 06:09:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-10-29 06:00:43 | Rathnapura (Kalu Ganga) | 5.10 | 🟢 Normal | -0.083 |  |
| 2026-10-29 07:02:48 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.087 |  |
| 2026-10-29 06:07:41 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)