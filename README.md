# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_11:27:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 11:27:22 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:13:28 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:11:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:11:06 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-29 11:10:55 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:10:28 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-29 11:10:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:09:31 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-29 11:08:59 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.047 |  |
| 2026-07-29 11:08:05 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:06:58 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-29 11:06:53 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-07-29 11:06:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-29 11:06:07 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:06:02 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.155 |  |
| 2026-07-29 11:05:54 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:04:44 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:04:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:04:02 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 11:03:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-29 11:03:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:03:16 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:54 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:35 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-29 11:02:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:07 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:57 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 11:01:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:49 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:01:34 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:01:18 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-29 11:01:13 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-29 11:01:01 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:00:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:00:36 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:00:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 11:06:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-29 11:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-29 11:03:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-29 11:10:28 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-29 11:06:58 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-29 11:02:35 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-29 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-29 11:01:18 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-29 11:00:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 11:00:36 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:04:44 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:01:34 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 11:01:57 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 11:04:02 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 11:11:06 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-29 11:02:54 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:04:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:49 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:10:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:13:28 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:06:07 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:05:54 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:09:31 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:01:01 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:11:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:03:16 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:10:55 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:27:22 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:02:07 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:08:05 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:01:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:01:13 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:00:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-07-29 11:06:53 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-07-29 11:08:59 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.047 |  |
| 2026-07-29 11:06:02 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)