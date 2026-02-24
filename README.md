# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_17:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 17:13:02 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:11:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:10:00 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:06:47 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:06:38 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:06:21 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-02-24 17:04:53 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:04:35 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:04:26 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:03:52 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:03:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-24 17:03:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:03:36 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-02-24 17:03:35 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:03:20 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-02-24 17:03:04 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 17:02:54 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-24 17:02:39 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-02-24 17:02:35 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:16 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-02-24 17:02:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:13 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:13 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:03 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:01:48 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:01:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-24 17:01:16 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:01:09 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:00:56 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:00:47 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:00:24 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:00:12 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.030 |  |
| 2026-02-24 16:37:36 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 17:01:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-24 17:03:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-24 17:02:54 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-24 16:15:42 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-24 17:03:04 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 17:02:03 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:00:56 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:03:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:13 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:35 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:01:36 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:01:48 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:04:53 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:00:47 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:02:13 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:13:02 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:06:47 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:10:00 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:11:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:06:21 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-02-24 17:03:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:03:35 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:06:38 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:01:26 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:01:09 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:00:24 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-24 17:03:52 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:14:54 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-02-24 17:03:36 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-02-24 17:03:20 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-02-24 17:04:35 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:04:26 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:01:16 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:02:39 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-02-24 17:02:16 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-02-24 17:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-02-24 17:00:12 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)