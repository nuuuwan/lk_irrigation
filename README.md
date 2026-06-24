# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_18:16:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 18:16:28 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:09:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:08:48 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-06-24 18:07:55 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:07:16 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:06:46 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:06:32 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.048 |  |
| 2026-06-24 18:06:25 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-06-24 18:05:29 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.060 |  |
| 2026-06-24 18:04:49 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-06-24 18:04:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:04:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:04:15 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-06-24 18:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:58 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:46 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.023 |  |
| 2026-06-24 18:03:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:29 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:03:28 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:26 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:18 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.064 |  |
| 2026-06-24 18:03:12 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:05 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:02:53 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:02:33 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:02:31 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-24 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.71 | 🟢 Normal | -0.091 |  |
| 2026-06-24 18:02:19 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:01:56 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:01:30 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:01:06 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.051 |  |
| 2026-06-24 18:00:49 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.041 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:33 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:00:20 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 18:02:19 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:07:16 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:03:05 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 18:02:53 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:58 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:06:46 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:12 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:00:33 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:09:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:02:33 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:04:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:28 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:16:28 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:01:30 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:04:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:29 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:03:26 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:01:56 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:08:48 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-06-24 18:02:31 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-24 18:04:49 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-06-24 18:03:46 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.023 |  |
| 2026-06-24 18:06:25 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-06-24 18:04:15 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-06-24 18:00:49 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.041 |  |
| 2026-06-24 18:06:32 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.048 |  |
| 2026-06-24 18:01:06 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.051 |  |
| 2026-06-24 18:05:29 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.060 |  |
| 2026-06-24 18:03:18 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.064 |  |
| 2026-06-24 18:00:20 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.065 |  |
| 2026-06-24 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.71 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)