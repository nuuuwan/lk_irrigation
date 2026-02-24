# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_19:21:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 19:21:14 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.016 |  |
| 2026-02-24 19:14:18 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:11:16 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-02-24 19:07:09 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-24 19:05:50 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-02-24 19:05:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:05:34 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:05:30 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:05:03 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 19:04:55 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-24 19:04:54 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-24 19:04:27 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:03:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-24 19:03:34 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:03:32 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-24 19:03:00 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 19:02:54 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:50 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:02:42 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 19:02:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:01:55 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:01:45 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:01:19 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-24 19:01:15 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-02-24 19:01:08 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:01:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:00:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:00:26 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:00:12 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:00:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.131 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 19:00:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-24 19:01:19 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-24 19:03:32 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-24 19:03:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-24 19:02:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 19:07:09 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-24 19:03:00 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 19:05:03 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 19:00:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:01:08 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:04:27 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:00:26 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:01:45 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:03:34 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:05:34 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:01:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:42 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:14:18 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:05:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:54 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:02:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 19:04:55 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-24 19:05:30 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:01:55 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:02:50 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:00:12 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:21:14 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.016 |  |
| 2026-02-24 19:04:54 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-24 19:05:50 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 19:01:15 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-24 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.053 |  |
| 2026-02-24 19:11:16 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)