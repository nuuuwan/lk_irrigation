# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_20:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 20:13:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:11:15 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:09:35 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-07-04 20:09:12 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:07:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:06:45 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 20:06:33 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:06:31 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-04 20:06:22 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-04 20:06:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:05:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:05:14 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:04:50 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:57 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:38 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:03:30 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:25 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-07-04 20:03:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-04 20:03:19 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-04 20:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 20:03:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-07-04 20:02:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:02:47 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 20:02:39 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 20:02:34 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.072 |  |
| 2026-07-04 20:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 20:02:11 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-07-04 20:01:51 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 1980.000 | 🔺 Rising |
| 2026-07-04 20:01:40 | Nakkala (Kumbukkan Oya) | 0.00 | 🟢 Normal | 1980.000 | 🔺 Rising |
| 2026-07-04 20:01:38 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 20:01:17 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:01:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:06 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.127 |  |
| 2026-07-04 20:00:18 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:00:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:33:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 20:01:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 1980.000 | 🔺 Rising |
| 2026-07-04 20:02:11 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-07-04 20:09:35 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-07-04 20:03:25 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-07-04 20:03:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-04 19:11:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 20:06:22 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-04 20:03:19 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-04 20:06:31 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-04 20:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 20:02:39 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 20:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 20:01:38 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 20:02:47 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 20:01:17 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:02:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:03:38 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:06:45 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:00:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:11:15 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:13:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:51 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:04:50 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:30 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:00:18 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:09:12 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:07:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:06:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:05:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:57 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:01:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:06:33 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:03:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-07-04 20:02:34 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.072 |  |
| 2026-07-04 20:01:06 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)