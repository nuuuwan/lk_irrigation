# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_12:14:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 12:14:44 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-06-10 12:11:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:10:21 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:07:32 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:07:30 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:06:39 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:05:43 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:05:38 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:05:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 12:05:09 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-06-10 12:04:44 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 12:04:24 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:04:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-06-10 12:04:07 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2026-06-10 12:03:43 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:38 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:34 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:20 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:12 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:02:48 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:42 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:42 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:02:30 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:01 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-10 12:02:01 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:48 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:48 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-06-10 12:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-10 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-10 12:01:24 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.020 |  |
| 2026-06-10 12:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:00:14 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-10 12:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-10 12:02:01 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-10 11:04:06 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-10 12:05:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 12:04:44 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 12:02:01 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:06:39 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:00:14 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:48 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:34 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:11:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:05:38 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:43 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:38 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:04:24 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:20 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:03:12 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:05:43 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:10:21 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:02:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:07:32 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 12:14:44 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-06-10 12:07:30 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:30 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:42 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:42 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:02:48 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-10 12:01:24 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.020 |  |
| 2026-06-10 12:01:48 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-06-10 12:04:07 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2026-06-10 12:05:09 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-06-10 12:04:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)