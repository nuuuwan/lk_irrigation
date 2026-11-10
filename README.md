# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_22:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,339 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 22:03:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-10 22:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-11-10 22:02:57 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 22:02:31 | Peradeniya (Mahaweli Ganga) | 5.72 | 🟡 Alert | -0.171 |  |
| 2026-11-10 22:02:16 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 22:02:14 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-10 22:02:00 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-11-10 22:02:00 | Moragaswewa (Deduru Oya) | 3.54 | 🟢 Normal | -0.082 |  |
| 2026-11-10 22:01:44 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | 0.082 | 🔺 Rising |
| 2026-11-10 22:01:22 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-11-10 22:01:14 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 22:01:12 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-11-10 22:00:33 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.087 |  |
| 2026-11-10 22:00:19 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 22:01:44 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | 0.082 | 🔺 Rising |
| 2026-11-10 21:08:48 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 22:02:16 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 21:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 21:02:04 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | -0.022 |  |
| 2026-11-10 21:05:13 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | 0.181 | 🔺 Rising |
| 2026-11-10 21:04:33 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-10 22:02:31 | Peradeniya (Mahaweli Ganga) | 5.72 | 🟡 Alert | -0.171 |  |
| 2026-11-10 21:09:06 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -216.000 |  |
| 2026-11-10 21:01:46 | Thawalama (Gin Ganga) | 3.81 | 🟢 Normal | 0.681 | 🔺 Rising |
| 2026-11-10 22:01:12 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-11-10 21:06:46 | Holombuwa (Kelani Ganga) | 2.76 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-11-10 22:03:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 21:05:38 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-10 22:02:57 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 21:04:55 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-10 22:01:14 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 21:03:49 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-10 21:15:42 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.003 |  |
| 2026-11-10 22:00:19 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:02:14 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 21:07:45 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-10 22:01:22 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-11-10 21:04:30 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-10 21:02:10 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-10 21:07:47 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.020 |  |
| 2026-11-10 21:03:48 | Hanwella (Kelani Ganga) | 4.39 | 🟢 Normal | -0.030 |  |
| 2026-11-10 21:02:42 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-11-10 22:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-11-10 22:02:00 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-11-10 22:02:00 | Moragaswewa (Deduru Oya) | 3.54 | 🟢 Normal | -0.082 |  |
| 2026-11-10 22:00:33 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.087 |  |
| 2026-11-10 21:03:47 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-11-10 21:02:06 | Moraketiya (Walawe Ganga) | 2.52 | 🟢 Normal | -0.164 |  |
| 2026-11-10 21:08:53 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)