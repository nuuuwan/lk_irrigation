# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_22:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 22:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 22:03:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:03:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-08 22:02:29 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-11-08 22:02:22 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:02:22 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.173 |  |
| 2026-11-08 22:02:21 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.061 |  |
| 2026-11-08 22:02:07 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:01:38 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:01:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-11-08 22:01:37 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 22:01:23 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:01:06 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 22:01:00 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-08 22:00:56 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | 0.000 |  |
| 2026-11-08 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 21:05:36 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | 0.531 | 🔺 Rising |
| 2026-11-08 22:02:29 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-11-08 21:07:37 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-08 21:09:20 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-08 22:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 22:00:56 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | 0.000 |  |
| 2026-11-08 22:02:21 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.061 |  |
| 2026-11-08 21:05:55 | Holombuwa (Kelani Ganga) | 3.35 | 🟡 Alert | -0.414 |  |
| 2026-11-08 21:05:05 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-11-08 21:04:55 | Glencourse (Kelani Ganga) | 13.23 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-11-08 22:01:00 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-08 22:03:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-08 21:04:47 | Rathnapura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-08 21:01:42 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-08 21:09:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 21:02:10 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 21:03:14 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 22:01:06 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 21:04:42 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 22:01:23 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:02:22 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 21:09:53 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 21:03:17 | Ellagawa (Kalu Ganga) | 8.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 22:01:37 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 21:04:16 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-08 21:05:59 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 21:02:42 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 21:11:19 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:01:38 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 21:02:08 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:03:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:02:07 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:01:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-11-08 21:00:53 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.091 |  |
| 2026-11-08 22:02:22 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)