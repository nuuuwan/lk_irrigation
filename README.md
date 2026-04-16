# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_18:12:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,842 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 18:12:28 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:11:24 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-04-16 18:10:53 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:10:35 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:09:19 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-16 18:08:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:08:23 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-04-16 18:08:13 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:06:54 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:06:43 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.116 |  |
| 2026-04-16 18:06:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:04:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:04:32 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.034 |  |
| 2026-04-16 18:04:00 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:03:50 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-04-16 18:03:43 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.064 |  |
| 2026-04-16 18:03:28 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:03:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 18:03:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-16 18:03:04 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:02:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:02:50 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:02:48 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-16 18:02:47 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 18:02:45 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:02:38 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-16 18:02:26 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.345 |  |
| 2026-04-16 18:02:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-04-16 18:02:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:02:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:01:29 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:01:28 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.106 |  |
| 2026-04-16 18:01:23 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-04-16 18:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:01:11 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:52 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -4.696 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 18:03:50 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-04-16 18:01:11 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-16 18:03:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-16 18:02:38 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-16 18:09:19 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-16 18:02:47 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 18:04:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:01:29 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:02:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:03:04 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:08:13 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:10:53 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:08:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:02:45 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:06:54 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:03:28 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:12:28 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:10:35 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:06:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:04:00 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:02:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:02:50 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:02:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:00:52 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-16 18:08:23 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-04-16 18:03:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 18:02:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-04-16 18:02:48 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-16 18:11:24 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-04-16 18:01:23 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-04-16 18:04:32 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.034 |  |
| 2026-04-16 18:03:43 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.064 |  |
| 2026-04-16 18:01:28 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.106 |  |
| 2026-04-16 18:06:43 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.116 |  |
| 2026-04-16 18:02:26 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.345 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)