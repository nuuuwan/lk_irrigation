# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_12:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,923 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 12:10:06 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:09:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:09:08 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-07-24 12:08:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:08:09 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:07:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.037 |  |
| 2026-07-24 12:07:35 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:47 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.028 |  |
| 2026-07-24 12:06:04 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:06:01 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 12:05:49 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:04:34 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-24 12:04:32 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.019 |  |
| 2026-07-24 12:03:52 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:52 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:18 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-07-24 12:03:05 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:02 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:55 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:18 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:14 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-07-24 12:02:08 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-07-24 12:02:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:56 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:47 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:47 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-24 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:23 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:19 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:00:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:00:09 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 12:01:47 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-24 12:04:34 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-24 12:06:01 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:00:09 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:05 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-24 11:41:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:02 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:47 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:56 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:52 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:07:35 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:09:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:00:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:08:09 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:08 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:19 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:03:52 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:06:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:01:47 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:10:06 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:02:18 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-24 12:08:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:01:23 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:06:04 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-07-24 12:04:32 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.019 |  |
| 2026-07-24 12:03:18 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-07-24 12:02:14 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-07-24 12:06:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.028 |  |
| 2026-07-24 12:09:08 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-07-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-07-24 12:07:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.037 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)