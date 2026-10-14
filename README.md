# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_22:09:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 22:09:20 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-10-14 22:08:45 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.047 |  |
| 2026-10-14 22:08:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:08:12 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:07:32 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 22:07:26 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-14 22:06:24 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:05:51 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:05:34 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-10-14 22:05:31 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-14 22:05:26 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.144 |  |
| 2026-10-14 22:05:04 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-10-14 22:04:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:04:07 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-14 22:03:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:03:52 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-14 22:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-10-14 22:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.000 |  |
| 2026-10-14 22:03:14 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.336 |  |
| 2026-10-14 22:03:13 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:02:46 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-10-14 22:02:41 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-10-14 22:02:29 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-14 22:02:23 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 22:02:10 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-14 22:02:09 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-14 22:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:02:08 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-14 22:02:07 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:01:33 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 22:00:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:00:15 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 21:07:56 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 21:08:49 | Holombuwa (Kelani Ganga) | 4.80 | 🟠 Minor Flood | -0.204 |  |
| 2026-10-14 21:06:46 | Rathnapura (Kalu Ganga) | 5.27 | 🟡 Alert | 0.508 | 🔺 Rising |
| 2026-10-14 21:22:08 | Panadugama (Nilwala Ganga) | 5.43 | 🟡 Alert | 0.000 |  |
| 2026-10-14 22:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.000 |  |
| 2026-10-14 21:06:56 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.088 |  |
| 2026-10-14 22:02:09 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-14 22:02:46 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-10-14 22:04:07 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-14 22:05:31 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-14 22:05:34 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-10-14 22:02:10 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-14 22:02:29 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-14 22:02:23 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 22:00:15 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 22:01:33 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 22:07:32 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:03:13 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:06:24 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:14:15 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:03:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:00:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:08:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:08:12 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:07:26 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:02:07 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:07:26 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-14 22:03:52 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-14 22:02:41 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-10-14 22:05:04 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-10-14 22:09:20 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-10-14 22:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-10-14 22:08:45 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.047 |  |
| 2026-10-14 22:05:26 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.144 |  |
| 2026-10-14 22:03:14 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.336 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)