# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_05:57:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,522 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 05:57:09 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.017 |  |
| 2026-06-17 05:52:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.093 |  |
| 2026-06-17 05:21:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.019 |  |
| 2026-06-17 05:16:57 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:16:08 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-17 05:15:26 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.041 |  |
| 2026-06-17 05:14:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-06-17 05:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 05:03:15 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-06-17 05:05:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 2.880 | 🔺 Rising |
| 2026-06-17 05:03:35 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-06-17 05:02:14 | Hanwella (Kelani Ganga) | 1.93 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-17 05:04:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 05:01:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:02:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:01:44 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:02:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:03:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:01:38 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:01:14 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:16:57 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:07:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:02:42 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:08:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:14:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-06-17 05:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.009 |  |
| 2026-06-17 05:16:08 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-17 05:02:25 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-17 05:06:19 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-17 05:03:13 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-06-17 05:02:54 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-17 05:06:53 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-06-17 05:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-06-17 05:01:12 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.015 |  |
| 2026-06-17 05:57:09 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.017 |  |
| 2026-06-17 05:21:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.019 |  |
| 2026-06-17 05:02:57 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-17 05:04:04 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-06-17 05:15:26 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.041 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-17 05:03:31 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.073 |  |
| 2026-06-17 05:02:11 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.080 |  |
| 2026-06-17 05:01:38 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.090 |  |
| 2026-06-17 04:05:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2026-06-17 05:52:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)