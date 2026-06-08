# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_16:00:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,897 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 16:00:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 16:00:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-08 16:00:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-06-08 15:58:59 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:14:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-08 15:12:09 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 15:11:57 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:11:11 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 15:14:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-08 15:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-08 15:02:03 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 15:12:09 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 15:04:37 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:02:12 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:02:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:02:07 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:01:35 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:04:37 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:03:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:11:57 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:02:24 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:00:09 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:04:09 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:01:33 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:04:59 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:00:48 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:02:48 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-08 16:00:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 15:05:39 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:05:35 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:04:53 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:08:12 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:02:04 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-06-08 16:00:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:04:36 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.010 |  |
| 2026-06-08 15:04:53 | Baddegama (Gin Ganga) | 2.69 | 🟢 Normal | -0.011 |  |
| 2026-06-08 15:11:11 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-06-08 15:04:10 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-06-08 15:07:43 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-06-08 15:06:10 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-08 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | -0.030 |  |
| 2026-06-08 15:02:39 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-06-08 16:00:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-06-08 15:08:22 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.034 |  |
| 2026-06-08 15:02:22 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.062 |  |
| 2026-06-08 15:01:09 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | -0.082 |  |
| 2026-06-08 15:08:53 | Rathnapura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)