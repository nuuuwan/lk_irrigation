# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_18:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 18:02:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-05-06 18:02:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-06 18:02:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:08 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-06 18:01:54 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:00:38 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-06 18:00:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2026-05-06 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:00:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 17:49:52 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:19:07 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:16:41 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-06 17:14:05 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:14:05 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 17:07:08 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-05-06 18:00:38 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-06 17:06:47 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-06 17:03:51 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 17:08:33 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 18:02:08 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-06 18:02:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:00:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 17:04:42 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 17:07:58 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 18:01:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:01:06 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:14:05 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:02:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:19:18 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:03:26 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:54 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:49:52 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:06:01 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:03:38 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:02:46 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 17:04:30 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 17:14:05 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-06 17:06:05 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.019 |  |
| 2026-05-06 18:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-05-06 17:02:41 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-05-06 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-06 17:06:38 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-05-06 17:02:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-06 17:01:09 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.039 |  |
| 2026-05-06 18:00:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)