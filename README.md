# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_11:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 11:17:39 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.024 |  |
| 2026-07-15 11:12:58 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-15 11:08:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:07:40 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 11:07:28 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-15 11:07:07 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-15 11:06:38 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:06:29 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:06:04 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-15 11:05:14 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-07-15 11:04:59 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-07-15 11:03:53 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:42 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:22 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:04 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-15 11:02:57 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:02:55 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-07-15 11:02:42 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:02:29 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:17 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:17 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:07 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-07-15 11:01:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:01:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:26 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 11:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:10 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:07 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 11:00:51 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:38 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:00:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:36 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:00:34 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:27 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 11:02:07 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-07-15 11:06:04 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-15 11:07:28 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-15 11:07:07 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-15 11:03:04 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-15 11:12:58 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-15 11:01:26 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 11:01:07 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 11:07:40 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 11:00:51 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:42 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:53 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:22 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:34 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:04:59 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:29 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:00:27 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:10 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:03:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:08:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:06:29 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:17 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:02:17 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 11:06:38 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:00:36 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:02:57 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:01:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:02:42 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-07-15 11:00:38 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-15 10:02:23 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-07-15 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-07-15 11:17:39 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.024 |  |
| 2026-07-15 11:02:55 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-07-15 11:05:14 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)