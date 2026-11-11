# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_21:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 21:03:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.063 |  |
| 2026-11-11 21:03:02 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-11-11 21:02:57 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-11 21:02:56 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-11 21:02:44 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-11-11 21:02:34 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | 0.151 | 🔺 Rising |
| 2026-11-11 21:02:28 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.042 |  |
| 2026-11-11 21:02:17 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | 0.261 | 🔺 Rising |
| 2026-11-11 21:02:14 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-11 21:02:11 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-11-11 21:02:04 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.680 | 🔺 Rising |
| 2026-11-11 21:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | -0.010 |  |
| 2026-11-11 21:01:45 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-11 21:01:06 | Moraketiya (Walawe Ganga) | 4.20 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-11-11 21:01:05 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 21:00:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-11 21:00:21 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 20:12:00 | Baddegama (Gin Ganga) | 4.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 20:18:58 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 21:02:17 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | 0.261 | 🔺 Rising |
| 2026-11-11 21:02:34 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | 0.151 | 🔺 Rising |
| 2026-11-11 21:01:06 | Moraketiya (Walawe Ganga) | 4.20 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-11-11 20:02:26 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 20:05:00 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | -0.010 |  |
| 2026-11-11 21:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | -0.010 |  |
| 2026-11-11 21:02:04 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.680 | 🔺 Rising |
| 2026-11-11 21:02:44 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-11-11 20:11:23 | Urawa (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-11-11 20:04:22 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-11 20:12:00 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-11 20:02:45 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-11 21:00:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-11 20:03:12 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-11 21:02:56 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-11 21:02:14 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-11 21:01:45 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-11 20:03:56 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-11 21:02:57 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-11 21:01:05 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 20:11:08 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 20:16:43 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 20:03:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 21:00:21 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-11 20:02:55 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 20:02:29 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-11-11 21:03:02 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-11-11 21:02:11 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-11-11 21:02:28 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.042 |  |
| 2026-11-11 20:03:11 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-11-11 21:03:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.063 |  |
| 2026-11-11 20:02:30 | Holombuwa (Kelani Ganga) | 2.23 | 🟢 Normal | -0.082 |  |
| 2026-11-11 20:08:22 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.114 |  |
| 2026-11-11 20:05:04 | Deraniyagala (Kelani Ganga) | 2.67 | 🟢 Normal | -0.664 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)