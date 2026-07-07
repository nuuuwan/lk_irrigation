# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_12:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 12:13:31 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.018 |  |
| 2026-07-07 12:09:20 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.074 |  |
| 2026-07-07 12:07:16 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:06:30 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-07-07 12:05:59 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.037 |  |
| 2026-07-07 12:05:42 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 12:05:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:27 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:03 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:04:08 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:04:02 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.011 |  |
| 2026-07-07 12:03:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.078 |  |
| 2026-07-07 12:03:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 12:03:26 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-07 12:03:24 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-07-07 12:03:20 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:03:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:55 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:02:46 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-07 12:02:42 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:36 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:02:35 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:35 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.130 |  |
| 2026-07-07 12:02:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-07 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-07 12:01:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-07-07 12:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:01:50 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:01:46 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-07 12:01:31 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:01:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.130 |  |
| 2026-07-07 12:01:03 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:00:36 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:35 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:21 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-07 12:01:46 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-07 12:02:46 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-07 12:02:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-07 12:03:26 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-07 12:03:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 12:05:42 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 12:00:36 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:36 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:07:16 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:01:03 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:03:20 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:04:08 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:01:31 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:03:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:35 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:02:42 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:03 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:00:21 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:05:27 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 12:06:30 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-07-07 12:02:55 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:01:50 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:00:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:01:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-07 12:04:02 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.011 |  |
| 2026-07-07 12:13:31 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.018 |  |
| 2026-07-07 12:05:59 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.037 |  |
| 2026-07-07 12:03:24 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-07-07 12:01:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-07-07 12:09:20 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.074 |  |
| 2026-07-07 12:03:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.078 |  |
| 2026-07-07 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.130 |  |
| 2026-07-07 12:02:35 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)