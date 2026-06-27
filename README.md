# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_21:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,085 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 21:10:21 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-06-27 21:10:00 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:07:39 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:07:21 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:06:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-06-27 21:06:44 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:06:43 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 21:05:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:05:46 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-06-27 21:05:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-06-27 21:05:23 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-27 21:05:09 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.049 |  |
| 2026-06-27 21:05:06 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:04:15 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 21:04:05 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.023 |  |
| 2026-06-27 21:03:31 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:03:22 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:03:13 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 21:03:00 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:02:17 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:09 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:06 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:03 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:01:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:01:54 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:01:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:01:20 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:01:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:00:24 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:00:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:00:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 21:05:23 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-27 21:06:43 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 21:04:15 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 21:03:13 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 21:02:03 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:01:54 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:07:39 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 21:02:09 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:00:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:00:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:07:21 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:01:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:01:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:03:31 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:17 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:05:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:10:00 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:01:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:06:44 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:06 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:05:06 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:03:22 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:03:00 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:10:21 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-06-27 21:05:46 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:02:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:00:24 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:01:20 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-27 21:05:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-06-27 21:04:05 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.023 |  |
| 2026-06-27 21:06:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-06-27 21:05:09 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)