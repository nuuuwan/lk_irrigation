# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_23:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Urawa — Alert; 🟡 Norwood — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 23:02:46 | Putupaula (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:40 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 23:02:29 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-11-12 23:02:15 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.072 |  |
| 2026-11-12 23:02:14 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.071 |  |
| 2026-11-12 23:02:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:02:05 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:02:04 | Peradeniya (Mahaweli Ganga) | 4.49 | 🟢 Normal | -0.081 |  |
| 2026-11-12 23:01:51 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.062 |  |
| 2026-11-12 23:01:18 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:01:01 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:00:55 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:00:39 | Nakkala (Kumbukkan Oya) | 2.13 | 🟢 Normal | -0.118 |  |
| 2026-11-12 23:00:39 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 22:05:35 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 23:01:18 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:00:55 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 22:13:00 | Urawa (Nilwala Ganga) | 2.95 | 🟡 Alert | 0.258 | 🔺 Rising |
| 2026-11-12 22:02:32 | Norwood (Kelani Ganga) | 1.70 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-12 22:01:59 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.010 |  |
| 2026-11-12 22:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.28 | 🟡 Alert | -0.011 |  |
| 2026-11-12 22:22:21 | Dunamale (Aththanagalu Oya) | 3.91 | 🟡 Alert | -0.030 |  |
| 2026-11-12 22:04:56 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -162.000 |  |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 22:02:09 | Thanamalwila (Kirindi Oya) | 2.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-12 23:02:40 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 22:05:19 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:02:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:01:01 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:02:05 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:46 | Putupaula (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-11-12 22:02:25 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:29 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-11-12 22:03:42 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-12 22:00:47 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-12 22:08:44 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-11-12 22:05:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-12 22:06:16 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | -0.030 |  |
| 2026-11-12 21:07:28 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.048 |  |
| 2026-11-12 23:01:51 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.062 |  |
| 2026-11-12 22:01:29 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.064 |  |
| 2026-11-12 22:03:27 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.069 |  |
| 2026-11-12 23:02:14 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.071 |  |
| 2026-11-12 23:02:15 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.072 |  |
| 2026-11-12 23:02:04 | Peradeniya (Mahaweli Ganga) | 4.49 | 🟢 Normal | -0.081 |  |
| 2026-11-12 22:05:35 | Wellawaya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.095 |  |
| 2026-11-12 22:03:00 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.099 |  |
| 2026-11-12 23:00:39 | Nakkala (Kumbukkan Oya) | 2.13 | 🟢 Normal | -0.118 |  |
| 2026-11-12 22:05:06 | Thaldena (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)