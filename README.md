# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_20:37:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 20:37:31 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:37:08 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.007 |  |
| 2026-04-16 20:27:21 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.007 |  |
| 2026-04-16 20:24:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:12:27 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-04-16 20:10:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:10:58 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.056 |  |
| 2026-04-16 20:09:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:09:52 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:06:54 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:06:17 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-16 20:05:44 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-04-16 20:04:52 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:04:42 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.049 |  |
| 2026-04-16 20:04:40 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 20:04:31 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.012 |  |
| 2026-04-16 20:03:59 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-16 20:03:33 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-16 20:03:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:03:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-16 20:03:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:03:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:54 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:45 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:24 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:12 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:11 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:02:03 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:49 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:47 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 20:01:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:31 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:21 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:59 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 20:03:33 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-16 20:01:47 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 20:04:40 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 20:06:17 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-16 20:09:52 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:03:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:59 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:31 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:54 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:03 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:49 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:03:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:12 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:24:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:37:31 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:45 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:03:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:02:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:01:21 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:10:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:09:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:27:21 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.007 |  |
| 2026-04-16 20:37:08 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.007 |  |
| 2026-04-16 20:12:27 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-04-16 20:04:31 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.012 |  |
| 2026-04-16 20:04:52 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:06:54 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:02:11 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-16 20:05:44 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-04-16 20:03:59 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-16 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-04-16 20:04:42 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.049 |  |
| 2026-04-16 20:10:58 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.056 |  |
| 2026-04-16 20:03:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)