# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_07:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 07:11:08 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:11:05 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:09:47 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:07:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-04-06 07:06:48 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.125 |  |
| 2026-04-06 07:06:26 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:06:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:06:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.119 |  |
| 2026-04-06 07:05:50 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.037 |  |
| 2026-04-06 07:05:49 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.094 |  |
| 2026-04-06 07:05:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-04-06 07:05:35 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:59 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-06 07:04:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:40 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:17 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:04:12 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-04-06 07:04:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:03:58 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:03:48 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:03:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-06 07:02:48 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:02:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-06 07:02:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:02:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.079 |  |
| 2026-04-06 07:02:10 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.072 |  |
| 2026-04-06 07:01:52 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-04-06 07:01:45 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-06 07:01:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:00:52 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-04-06 07:00:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-04-06 07:00:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:00:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:42:59 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 07:01:45 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-06 07:04:59 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-06 06:01:56 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 07:03:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-06 07:04:17 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:04:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:06:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 07:02:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:02:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:03:58 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:11:05 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:40 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:05:35 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:01:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:04:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:11:08 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:06:26 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:09:47 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:07:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-04-06 07:00:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:03:48 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:02:48 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:00:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-06 07:02:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-06 07:04:12 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-04-06 07:01:52 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-04-06 07:05:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-04-06 07:05:50 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.037 |  |
| 2026-04-06 07:00:52 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-04-06 07:02:10 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.072 |  |
| 2026-04-06 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.079 |  |
| 2026-04-06 07:05:49 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.094 |  |
| 2026-04-06 07:00:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-04-06 07:06:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.119 |  |
| 2026-04-06 07:06:48 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)