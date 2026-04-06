# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_16:15:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 16:15:34 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:12:19 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 16:10:30 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-06 16:09:23 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:08:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:07:19 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-06 16:06:49 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:06:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-04-06 16:06:00 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 16:05:30 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-06 16:04:55 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 16:04:20 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 16:03:53 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:03:48 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:03:46 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-06 16:03:39 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 16:03:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 16:03:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-04-06 16:03:02 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:51 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:47 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:42 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 16:02:33 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:02:25 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:17 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:16 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.108 |  |
| 2026-04-06 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-06 16:02:11 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:07 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:01:45 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-06 16:01:41 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:01:32 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.022 |  |
| 2026-04-06 16:01:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-06 16:00:44 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:00:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 16:05:30 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-06 16:01:45 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-06 16:10:30 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-06 16:04:55 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 16:06:00 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 16:04:20 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 16:02:42 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 16:03:39 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 16:03:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 16:12:19 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 16:02:47 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:00:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:07 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:01:41 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:11 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:07:40 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:17 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:15:34 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:03:48 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:03:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:25 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:51 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:03:02 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:06:49 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:08:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:09:23 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:03:53 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:02:33 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:00:44 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:04:03 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:01:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-06 16:07:19 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-06 16:06:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-04-06 16:03:46 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-06 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-06 16:01:32 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.022 |  |
| 2026-04-06 16:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-04-06 16:02:16 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)