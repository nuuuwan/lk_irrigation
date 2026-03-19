# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_08:06:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,416 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 08:06:03 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-19 08:05:49 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.114 |  |
| 2026-03-19 08:05:44 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.043 |  |
| 2026-03-19 08:05:32 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-19 08:04:47 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:23 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:15 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 08:03:50 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 08:03:46 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:38 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-03-19 08:03:33 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.121 |  |
| 2026-03-19 08:03:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-19 08:03:19 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:11 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:05 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 08:02:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.083 |  |
| 2026-03-19 08:02:27 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 08:02:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:02:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-19 08:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-19 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 08:01:26 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:17 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:00:26 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.041 |  |
| 2026-03-19 07:28:59 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:17:25 | Urawa (Nilwala Ganga) | -0.19 | 🟢 Normal | -0.219 |  |
| 2026-03-19 07:14:58 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:13:22 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 07:05:42 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-03-19 08:02:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-19 08:05:32 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-19 08:06:03 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-19 08:04:15 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 08:03:50 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 07:05:47 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 08:02:27 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 07:10:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-19 08:01:17 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 08:03:05 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 08:01:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:02:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:01:01 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:47 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:23 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:19 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:06:52 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:46 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:28:59 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:04:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 07:09:30 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:11 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:01:26 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:05:49 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:03:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-19 07:04:34 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-19 08:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-19 08:00:26 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.041 |  |
| 2026-03-19 08:05:44 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.043 |  |
| 2026-03-19 08:03:38 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-03-19 07:13:22 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.072 |  |
| 2026-03-19 08:02:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.083 |  |
| 2026-03-19 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.114 |  |
| 2026-03-19 08:03:33 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.121 |  |
| 2026-03-19 07:17:25 | Urawa (Nilwala Ganga) | -0.19 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)