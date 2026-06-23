# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_20:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 20:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.011 |  |
| 2026-06-23 20:06:43 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:06:08 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-06-23 20:06:05 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.031 |  |
| 2026-06-23 20:05:52 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-06-23 20:05:45 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:05:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:05:22 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-23 20:04:52 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:04:49 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.131 |  |
| 2026-06-23 20:04:45 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.039 |  |
| 2026-06-23 20:04:13 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:04:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:04:00 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.087 |  |
| 2026-06-23 20:03:37 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 20:03:37 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.073 |  |
| 2026-06-23 20:03:18 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:03:17 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.059 |  |
| 2026-06-23 20:03:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:02:33 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:02:28 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-06-23 20:02:07 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:52 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:01:48 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:42 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:27 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-23 20:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:09 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | -0.068 |  |
| 2026-06-23 20:01:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:00:47 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:00:19 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:23:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 20:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.011 |  |
| 2026-06-23 20:03:17 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.059 |  |
| 2026-06-23 20:05:22 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-23 20:03:37 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 20:02:33 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:02:07 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:48 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:03:18 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:04:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:06:43 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:03:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:04:52 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:00:19 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:01:42 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:05:45 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:00:47 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 20:05:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:04:13 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:01:52 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-23 20:01:27 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-23 19:05:05 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-06-23 19:05:40 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.029 |  |
| 2026-06-23 20:06:08 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-06-23 20:06:05 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.031 |  |
| 2026-06-23 20:05:52 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-06-23 20:04:45 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.039 |  |
| 2026-06-23 20:02:28 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-06-23 20:01:09 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | -0.068 |  |
| 2026-06-23 20:03:37 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.073 |  |
| 2026-06-23 20:04:00 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.087 |  |
| 2026-06-23 19:08:57 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.107 |  |
| 2026-06-23 20:04:49 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)