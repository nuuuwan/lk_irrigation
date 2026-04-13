# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_23:07:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 23:07:30 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:07:22 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:06:55 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 23:06:24 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-13 23:06:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:06:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-04-13 23:04:47 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 23:04:27 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 23:04:14 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:03:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:03:58 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-04-13 23:03:36 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:03:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:03:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:02:51 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:02:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-13 23:02:22 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-13 23:02:10 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:01:31 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.173 |  |
| 2026-04-13 23:01:26 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:01:19 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-13 23:01:17 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-04-13 23:00:51 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:00:45 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:00:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:59:13 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 22:06:36 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-13 23:02:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-13 23:06:55 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 22:07:29 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-13 23:02:22 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-13 23:01:19 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-13 22:59:13 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 23:04:47 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 23:04:27 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 23:00:51 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:06:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:00:39 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:03:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:01:26 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:00:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:07:22 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:02:10 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:03:36 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:01:26 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:03:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:00:45 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:07:30 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:04:14 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:02:51 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:03:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-13 23:03:58 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-04-13 22:09:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-04-13 23:01:17 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-04-13 21:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-04-13 23:06:24 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-13 23:06:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-04-13 22:03:39 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.066 |  |
| 2026-04-13 21:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.079 |  |
| 2026-04-13 21:00:31 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-13 21:10:02 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.098 |  |
| 2026-04-13 23:01:31 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)