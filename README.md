# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_22:20:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 22:20:03 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-01-11 22:15:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-01-11 22:12:25 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:09:53 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 22:09:48 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-11 22:08:48 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-11 22:07:35 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:07:24 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-11 22:06:47 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-11 22:06:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-01-11 22:05:49 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:05:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:04:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:04:08 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 22:04:07 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 22:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 22:03:48 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 22:03:38 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:03:24 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 22:03:07 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:02:51 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 22:02:45 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-11 22:02:41 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:02:33 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-11 22:02:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-11 22:02:30 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 22:02:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:01:32 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:01:31 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 22:01:29 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:01:12 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:58 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:43 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:23 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 22:20:03 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-01-11 22:08:48 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-11 22:06:47 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-11 22:02:33 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-11 22:09:48 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-11 22:03:24 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 22:02:51 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 22:04:08 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 22:03:48 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 22:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 22:01:31 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 22:09:53 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 22:07:24 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-11 22:04:07 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 22:02:30 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:58 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:01:12 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:03:07 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:02:41 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:02:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:12:25 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:05:49 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:23 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:04:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:00:43 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:05:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:07:35 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:01:32 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:01:29 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:03:38 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-11 22:02:45 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-11 22:06:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-01-11 22:02:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-11 22:15:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)