# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_04:18:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,296 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 04:18:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-16 04:08:14 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:08:04 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 04:06:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:05:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.011 |  |
| 2026-04-16 04:05:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-04-16 04:05:19 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:04:47 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-16 04:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-16 04:04:33 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-16 04:04:30 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-16 04:04:14 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.132 |  |
| 2026-04-16 04:03:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 04:03:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-16 04:03:38 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-16 04:03:26 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-16 04:03:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 04:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-04-16 04:03:09 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:02:54 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:02:40 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 04:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:41 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-04-16 04:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:27 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-04-16 04:01:23 | Kuda Oya (Kirindi Oya) | 2.80 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-04-16 04:01:04 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:00:58 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -2.006 |  |
| 2026-04-16 04:00:27 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 03:56:41 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 04:01:23 | Kuda Oya (Kirindi Oya) | 2.80 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-04-16 04:18:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-16 04:01:41 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-04-16 04:04:47 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-16 04:04:30 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-16 04:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-16 04:02:40 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 04:04:33 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-16 04:03:38 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 03:10:28 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 04:08:04 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 04:00:27 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 04:03:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 04:03:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 04:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:02:54 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:03:09 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:04 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:08:14 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:05:19 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:06:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:27 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-04-16 04:03:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-16 04:05:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.011 |  |
| 2026-04-16 04:03:26 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-16 04:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-16 04:05:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 04:04:14 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.132 |  |
| 2026-04-16 03:00:16 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.528 |  |
| 2026-04-16 04:00:58 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -2.006 |  |
| 2026-04-16 03:16:18 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)