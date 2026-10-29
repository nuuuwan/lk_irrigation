# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_03:03:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 03:03:34 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-10-30 03:03:27 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.099 |  |
| 2026-10-30 03:03:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:03:09 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.071 |  |
| 2026-10-30 03:02:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:42 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.084 |  |
| 2026-10-30 03:02:32 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:18 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 03:02:17 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-30 03:02:15 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-30 03:02:12 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:01:53 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.010 |  |
| 2026-10-30 03:01:32 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:00:18 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-30 03:00:14 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 02:59:03 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 02:56:12 | Putupaula (Kalu Ganga) | 3.61 | 🟡 Alert | -0.004 |  |
| 2026-10-30 02:46:13 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.071 |  |
| 2026-10-30 02:39:41 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-30 02:29:14 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-10-30 02:27:01 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 03:02:18 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 01:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-30 02:56:12 | Putupaula (Kalu Ganga) | 3.61 | 🟡 Alert | -0.004 |  |
| 2026-10-30 02:07:33 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | -0.011 |  |
| 2026-10-30 02:04:05 | Baddegama (Gin Ganga) | 3.74 | 🟡 Alert | -0.021 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-30 02:06:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-30 02:03:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 03:02:17 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-30 02:02:50 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:00:14 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:32 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:01:32 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 02:03:57 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 01:04:23 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:04:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:42 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:03:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:02:12 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-30 01:09:51 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-30 01:21:59 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.004 |  |
| 2026-10-30 02:12:30 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-10-30 02:04:31 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 03:02:15 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-30 03:01:53 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.010 |  |
| 2026-10-30 02:04:58 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.011 |  |
| 2026-10-30 02:00:54 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.011 |  |
| 2026-10-30 01:12:18 | Pitabeddara (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.019 |  |
| 2026-10-30 03:00:18 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-30 00:09:36 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.035 |  |
| 2026-10-30 03:03:34 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-10-30 02:01:32 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.040 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-30 03:03:09 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.071 |  |
| 2026-10-30 03:02:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.084 |  |
| 2026-10-30 03:03:27 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)