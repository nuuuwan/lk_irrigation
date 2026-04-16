# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_11:17:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 11:17:55 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -36.000 |  |
| 2026-04-16 11:17:53 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -36.000 |  |
| 2026-04-16 11:12:45 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-04-16 11:10:59 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.055 |  |
| 2026-04-16 11:09:23 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-04-16 11:08:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:08:10 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:07:50 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-04-16 11:07:47 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-16 11:07:02 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.104 |  |
| 2026-04-16 11:06:19 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:06:17 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:05:40 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.037 |  |
| 2026-04-16 11:05:33 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:05:29 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-16 11:05:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:04:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:04:04 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-16 11:03:54 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.029 |  |
| 2026-04-16 11:03:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-16 11:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:35 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-16 11:03:27 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-04-16 11:03:22 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:06 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-16 11:02:54 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-04-16 11:02:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 11:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-16 11:02:24 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:02:11 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.080 |  |
| 2026-04-16 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.060 |  |
| 2026-04-16 11:01:53 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-16 11:01:09 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:00:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:00:19 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 10:37:42 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 11:02:54 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-04-16 11:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-16 11:05:29 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-16 11:00:19 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 11:03:06 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-16 11:02:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 11:01:53 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:00:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:05:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:06:19 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:08:50 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:01:09 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:02:24 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:22 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:04:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:06:17 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:05:33 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:08:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:08:10 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:03:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 11:07:47 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-16 11:03:35 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-16 11:03:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-16 11:12:45 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-04-16 11:09:23 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-04-16 11:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-16 11:04:04 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-16 11:03:54 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.029 |  |
| 2026-04-16 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-16 11:05:40 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.037 |  |
| 2026-04-16 11:07:50 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-04-16 11:03:27 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-04-16 11:10:59 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.055 |  |
| 2026-04-16 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.060 |  |
| 2026-04-16 11:02:11 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.080 |  |
| 2026-04-16 11:07:02 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.104 |  |
| 2026-04-16 11:17:55 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)