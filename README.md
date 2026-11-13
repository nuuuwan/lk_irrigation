# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_18:32:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 18:32:55 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -72.000 |  |
| 2026-11-13 18:32:53 | Pitabeddara (Nilwala Ganga) | 1.91 | 🟢 Normal | -72.000 |  |
| 2026-11-13 18:09:11 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.035 |  |
| 2026-11-13 18:09:07 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -0.041 |  |
| 2026-11-13 18:08:46 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:08:44 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:07:10 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:06:17 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-11-13 18:05:12 | Ellagawa (Kalu Ganga) | 7.57 | 🟢 Normal | -0.066 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:35 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-13 18:04:30 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.050 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:04:00 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.060 |  |
| 2026-11-13 18:03:49 | Kuda Oya (Kirindi Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-11-13 18:03:44 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:03:12 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:03:02 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-13 18:02:49 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 18:02:33 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:02:24 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.056 |  |
| 2026-11-13 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.040 |  |
| 2026-11-13 18:02:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:02:13 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-13 18:01:55 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.126 |  |
| 2026-11-13 18:01:51 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.032 |  |
| 2026-11-13 18:01:49 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | 0.000 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 18:01:43 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:01:26 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.041 |  |
| 2026-11-13 18:01:25 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 18:01:08 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.082 |  |
| 2026-11-13 18:00:57 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:00:34 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.034 |  |
| 2026-11-13 18:00:27 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-13 18:00:23 | Horowpothana (Yan Oya) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-11-13 18:00:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-11-13 18:00:12 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | -0.022 |  |
| 2026-11-13 18:00:08 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-11-13 18:00:05 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 18:01:25 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 18:00:12 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | -0.022 |  |
| 2026-11-13 18:09:11 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.035 |  |
| 2026-11-13 18:01:49 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | 0.000 |  |
| 2026-11-13 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.040 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:01:43 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:08:44 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:03:49 | Kuda Oya (Kirindi Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-11-13 18:06:17 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-11-13 18:03:02 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-13 18:00:27 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-13 18:00:05 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-11-13 18:00:08 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-11-13 18:00:23 | Horowpothana (Yan Oya) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-11-13 18:08:46 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:02:33 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:02:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:00:57 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:07:10 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:03:12 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-11-13 18:01:51 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.032 |  |
| 2026-11-13 18:00:34 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.034 |  |
| 2026-11-13 18:02:13 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-13 18:01:26 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.041 |  |
| 2026-11-13 18:09:07 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -0.041 |  |
| 2026-11-13 18:02:49 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 18:04:30 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.050 |  |
| 2026-11-13 18:04:35 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-13 18:02:24 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.056 |  |
| 2026-11-13 18:04:00 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.060 |  |
| 2026-11-13 18:05:12 | Ellagawa (Kalu Ganga) | 7.57 | 🟢 Normal | -0.066 |  |
| 2026-11-13 18:01:08 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.082 |  |
| 2026-11-13 18:00:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-11-13 18:01:55 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.126 |  |
| 2026-11-13 18:32:55 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)