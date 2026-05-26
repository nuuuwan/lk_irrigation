# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_18:07:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 18:07:31 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 18:07:10 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | -0.065 |  |
| 2026-05-26 18:06:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:06:07 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:06:07 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.023 |  |
| 2026-05-26 18:05:57 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 18:05:50 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:05:10 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.021 |  |
| 2026-05-26 18:04:55 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.054 |  |
| 2026-05-26 18:04:53 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-05-26 18:04:44 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:41 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:38 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:03:52 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:03:51 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:03:48 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-05-26 18:03:40 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.029 |  |
| 2026-05-26 18:03:37 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | -0.035 |  |
| 2026-05-26 18:03:20 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-05-26 18:03:12 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:03:09 | Hanwella (Kelani Ganga) | 4.73 | 🟢 Normal | -0.040 |  |
| 2026-05-26 18:02:59 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:02:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:02:40 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:02:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:02:04 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:59 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:36 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:25 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:00:10 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 17:33:04 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 18:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-05-26 18:07:31 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 18:05:57 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 18:03:20 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:06:07 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:01:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:36 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:59 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:06:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:02:04 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:44 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:05:50 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 17:07:20 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:41 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:02:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:38 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 17:11:37 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:01:25 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:04:53 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-05-26 18:03:51 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:03:52 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:02:40 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:00:10 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:02:59 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:02:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:03:12 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:05:10 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.021 |  |
| 2026-05-26 18:03:48 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-05-26 18:06:07 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.023 |  |
| 2026-05-26 18:03:40 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.029 |  |
| 2026-05-26 18:03:37 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | -0.035 |  |
| 2026-05-26 18:03:09 | Hanwella (Kelani Ganga) | 4.73 | 🟢 Normal | -0.040 |  |
| 2026-05-26 18:04:55 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.054 |  |
| 2026-05-26 18:07:10 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)