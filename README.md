# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_05:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 05:02:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-11 05:02:43 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:02:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.066 |  |
| 2026-11-11 05:02:27 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.061 |  |
| 2026-11-11 05:02:24 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:02:03 | Thawalama (Gin Ganga) | 3.63 | 🟢 Normal | -0.190 |  |
| 2026-11-11 05:02:00 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.197 |  |
| 2026-11-11 05:01:36 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-11 05:01:34 | Kuda Oya (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-11 05:01:29 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:01:25 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.182 |  |
| 2026-11-11 05:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-11 05:00:12 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.220 |  |
| 2026-11-11 05:00:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-11 05:00:07 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 04:45:31 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-11 04:38:07 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 04:35:26 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.014 |  |
| 2026-11-11 04:28:11 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 04:09:11 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:00:07 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 04:28:11 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 04:06:20 | Dunamale (Aththanagalu Oya) | 4.31 | 🟡 Alert | -0.019 |  |
| 2026-11-11 03:11:08 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-11-11 04:06:34 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | 0.543 | 🔺 Rising |
| 2026-11-11 05:00:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-11 04:05:37 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 04:02:50 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-11 04:05:37 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 04:45:31 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-11 05:01:29 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 04:03:19 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 04:01:19 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:02:24 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 04:02:46 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-11 05:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-11 04:35:26 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.014 |  |
| 2026-11-11 04:21:07 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.015 |  |
| 2026-11-11 05:01:36 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-11 05:02:43 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-11 04:03:51 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.033 |  |
| 2026-11-11 05:01:34 | Kuda Oya (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-11 04:09:53 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.057 |  |
| 2026-11-11 05:02:27 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.061 |  |
| 2026-11-11 05:02:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.066 |  |
| 2026-11-11 04:10:48 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.075 |  |
| 2026-11-11 04:04:38 | Rathnapura (Kalu Ganga) | 5.12 | 🟢 Normal | -0.108 |  |
| 2026-11-11 05:02:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-11 04:18:21 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.141 |  |
| 2026-11-11 04:03:57 | Giriulla (Maha Oya) | 3.98 | 🟢 Normal | -0.178 |  |
| 2026-11-11 05:01:25 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.182 |  |
| 2026-11-11 05:02:03 | Thawalama (Gin Ganga) | 3.63 | 🟢 Normal | -0.190 |  |
| 2026-11-11 05:02:00 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.197 |  |
| 2026-11-11 05:00:12 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)