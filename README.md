# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_17:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 17:16:19 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-06 17:14:34 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 17:09:36 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:09:27 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 17:09:21 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 17:09:19 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:08:49 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-02-06 17:08:04 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:06:42 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 17:06:12 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:05:42 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:05:12 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:39 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-06 17:04:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:20 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:20 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 17:04:14 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:03:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:03:42 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-06 17:03:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:03:30 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-02-06 17:02:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:02:44 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 17:02:33 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:02:27 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-06 17:02:21 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:02:04 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:01:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-02-06 17:01:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-06 17:01:12 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:00:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 17:08:49 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 17:09:21 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 17:02:27 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-06 17:16:19 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-06 17:04:20 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 15:09:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-06 17:01:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-06 17:03:42 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-06 17:06:42 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 17:09:27 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 17:02:44 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 17:14:34 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 17:02:04 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:20 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:05:42 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:08:04 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:02:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:02:33 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:05:12 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:09:19 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:04:14 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 16:05:05 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 16:02:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:06:12 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:09:36 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:03:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-06 17:02:21 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:00:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:03:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:01:12 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:04:39 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-06 17:03:30 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-02-06 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.060 |  |
| 2026-02-06 17:01:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)