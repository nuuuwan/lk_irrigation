# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_18:29:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 18:29:26 | Moragaswewa (Deduru Oya) | 4.72 | 🟢 Normal | -0.055 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 18:10:24 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:07:46 | Dunamale (Aththanagalu Oya) | 4.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 18:07:41 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-10-27 18:07:34 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:07:01 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:06:43 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:06:41 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | -0.088 |  |
| 2026-10-27 18:05:43 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-10-27 18:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:03:21 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-27 18:03:17 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-10-27 18:03:11 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.098 |  |
| 2026-10-27 18:03:00 | Hanwella (Kelani Ganga) | 5.39 | 🟢 Normal | -0.109 |  |
| 2026-10-27 18:02:58 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 18:02:58 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.059 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.65 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 18:02:12 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:02:10 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-10-27 18:02:10 | Rathnapura (Kalu Ganga) | 7.82 | 🟠 Minor Flood | -0.080 |  |
| 2026-10-27 18:02:04 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-10-27 18:01:43 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-27 18:01:41 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:01:40 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 18:01:39 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.060 |  |
| 2026-10-27 18:01:35 | Glencourse (Kelani Ganga) | 12.26 | 🟢 Normal | -0.143 |  |
| 2026-10-27 18:01:29 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.070 |  |
| 2026-10-27 18:01:28 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:01:24 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-27 18:01:22 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 18:01:13 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.032 |  |
| 2026-10-27 18:01:09 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:00:59 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:00:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-10-27 18:00:46 | Dunamale (Aththanagalu Oya) | 4.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 18:00:32 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.070 |  |
| 2026-10-27 18:00:16 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:00:13 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.65 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 18:01:43 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-27 18:07:46 | Dunamale (Aththanagalu Oya) | 4.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 18:03:21 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-27 18:02:10 | Rathnapura (Kalu Ganga) | 7.82 | 🟠 Minor Flood | -0.080 |  |
| 2026-10-27 18:02:58 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 18:01:40 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 18:00:13 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-27 18:00:32 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.070 |  |
| 2026-10-27 18:01:22 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 18:01:09 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:01:41 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:10:24 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:02:12 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:07:01 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:00:59 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 18:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:07:34 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:00:16 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:01:28 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:07:41 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-10-27 18:05:43 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-10-27 18:03:17 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-10-27 18:00:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-10-27 18:02:04 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-10-27 18:01:24 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-27 18:01:13 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.032 |  |
| 2026-10-27 18:02:10 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-10-27 18:29:26 | Moragaswewa (Deduru Oya) | 4.72 | 🟢 Normal | -0.055 |  |
| 2026-10-27 18:02:58 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.059 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 18:01:39 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.060 |  |
| 2026-10-27 18:01:29 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.070 |  |
| 2026-10-27 18:06:41 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | -0.088 |  |
| 2026-10-27 18:03:11 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.098 |  |
| 2026-10-27 18:03:00 | Hanwella (Kelani Ganga) | 5.39 | 🟢 Normal | -0.109 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 18:01:35 | Glencourse (Kelani Ganga) | 12.26 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)