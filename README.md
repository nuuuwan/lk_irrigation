# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_09:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 09:13:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.087 |  |
| 2026-05-18 09:08:43 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-05-18 09:08:38 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.019 |  |
| 2026-05-18 09:07:36 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:07:02 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 09:06:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.015 |  |
| 2026-05-18 09:06:33 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 09:06:24 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-05-18 09:05:15 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 09:05:11 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:05:03 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:04:37 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-18 09:04:23 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-05-18 09:04:14 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-05-18 09:03:54 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.064 |  |
| 2026-05-18 09:03:54 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.033 |  |
| 2026-05-18 09:03:28 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.039 |  |
| 2026-05-18 09:03:25 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:03:12 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:03:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:03:11 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | -0.041 |  |
| 2026-05-18 09:02:59 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.025 |  |
| 2026-05-18 09:02:59 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:02:56 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.049 |  |
| 2026-05-18 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.059 |  |
| 2026-05-18 09:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:02:06 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.062 |  |
| 2026-05-18 09:01:59 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:01:44 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.091 |  |
| 2026-05-18 09:01:41 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:01:39 | Thanthirimale (Malwathu Oya) | 3.22 | 🟢 Normal | -0.061 |  |
| 2026-05-18 09:01:33 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-18 09:00:11 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-18 08:55:33 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 08:39:59 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 08:26:53 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.059 |  |
| 2026-05-18 09:06:33 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 09:07:02 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 08:08:51 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-18 09:05:15 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 09:03:25 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:07:36 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 08:55:33 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:02:59 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 08:06:42 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:05:03 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:01:41 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:03:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:01:59 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:04:37 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-18 09:05:11 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:00:11 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:03:12 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-18 09:06:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.015 |  |
| 2026-05-18 09:08:38 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.019 |  |
| 2026-05-18 09:06:24 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-05-18 09:00:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-18 09:02:59 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.025 |  |
| 2026-05-18 09:08:43 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-05-18 09:03:54 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.033 |  |
| 2026-05-18 09:03:28 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.039 |  |
| 2026-05-18 09:03:11 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | -0.041 |  |
| 2026-05-18 09:02:56 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.049 |  |
| 2026-05-18 09:04:23 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-05-18 09:04:14 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-05-18 09:01:39 | Thanthirimale (Malwathu Oya) | 3.22 | 🟢 Normal | -0.061 |  |
| 2026-05-18 09:02:06 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.062 |  |
| 2026-05-18 09:03:54 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.064 |  |
| 2026-05-18 09:13:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.087 |  |
| 2026-05-18 09:01:44 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)