# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_22:03:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,527 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 22:03:39 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:03:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.107 |  |
| 2026-06-23 22:02:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-06-23 22:02:56 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.020 |  |
| 2026-06-23 22:02:54 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:31 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | -0.032 |  |
| 2026-06-23 22:02:15 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:49 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.052 |  |
| 2026-06-23 22:01:49 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:43 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:35 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:13 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:12 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:07 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:02 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:00:45 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:00:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 21:14:23 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 21:13:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.027 |  |
| 2026-06-23 22:02:31 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | -0.032 |  |
| 2026-06-23 22:02:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-06-23 21:08:47 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 22:01:12 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:02 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:13 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:43 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:54 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:00:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 21:13:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:35 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:07 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:03:39 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:15 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 21:02:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:01:49 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 21:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-23 21:04:58 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-06-23 21:05:32 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 21:01:23 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.013 |  |
| 2026-06-23 22:02:56 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.020 |  |
| 2026-06-23 21:01:33 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-06-23 21:04:01 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.022 |  |
| 2026-06-23 21:08:36 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.032 |  |
| 2026-06-23 21:13:22 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | -0.035 |  |
| 2026-06-23 21:05:33 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-23 21:02:51 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.042 |  |
| 2026-06-23 21:14:23 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.043 |  |
| 2026-06-23 21:06:46 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.046 |  |
| 2026-06-23 22:01:49 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.052 |  |
| 2026-06-23 21:10:02 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.100 |  |
| 2026-06-23 22:03:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.107 |  |
| 2026-06-23 21:05:28 | Hanwella (Kelani Ganga) | 3.71 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)