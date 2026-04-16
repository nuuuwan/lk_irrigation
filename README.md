# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_16:19:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 16:19:47 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:12:17 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:11:45 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:11:27 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:10:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:10:07 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:09:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:56 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:04 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:03 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-16 16:07:52 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-04-16 16:07:29 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.019 |  |
| 2026-04-16 16:07:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:06:54 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 16:05:59 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-16 16:05:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:05:22 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-16 16:05:21 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:04:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:03:30 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.051 |  |
| 2026-04-16 16:03:15 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:03:04 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.105 |  |
| 2026-04-16 16:03:02 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.080 |  |
| 2026-04-16 16:02:39 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 16:02:38 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:02:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:02:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-04-16 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-04-16 16:02:04 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:01:55 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-16 16:01:39 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:01:32 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-16 16:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:01:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.124 |  |
| 2026-04-16 16:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 16:00:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:00:31 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-04-16 16:00:15 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 16:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 15:05:06 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-16 16:05:59 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-16 16:08:03 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-16 16:02:39 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 16:06:54 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 16:01:39 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:02:04 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:00:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:12:17 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:09:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:02:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:11:45 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:19:47 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:05:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:10:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:04:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:02:38 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:05:21 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:03:15 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:56 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:08:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:11:27 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:07:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:10:07 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-04-16 16:01:55 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-16 16:01:32 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-16 16:07:29 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.019 |  |
| 2026-04-16 16:07:52 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-04-16 16:02:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-04-16 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-04-16 16:00:31 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-04-16 16:05:22 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-16 16:03:30 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.051 |  |
| 2026-04-16 16:00:15 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.080 |  |
| 2026-04-16 16:03:02 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.080 |  |
| 2026-04-16 16:03:04 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.105 |  |
| 2026-04-16 16:01:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)