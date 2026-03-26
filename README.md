# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_22:16:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,225 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 22:16:22 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-26 22:11:04 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:10:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:09:36 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:09:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:07:30 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-26 22:07:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:07:12 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:05:52 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-26 22:05:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-03-26 22:05:07 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:46 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-26 22:04:38 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:26 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-03-26 22:04:05 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:03:55 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.097 |  |
| 2026-03-26 22:03:30 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:03:01 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.051 |  |
| 2026-03-26 22:02:31 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:29 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:28 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:16 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:16 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-26 22:01:05 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:55 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:47 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 22:01:16 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-26 21:07:10 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-26 22:16:22 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-26 21:06:45 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-26 22:01:05 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:10:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:38 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:55 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 18:01:41 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 21:13:23 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:03:30 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:31 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:09:36 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:09:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:05 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:01:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:26 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:07:12 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:07:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:28 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:00:47 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:11:04 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-26 21:03:35 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:05:07 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:02:16 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 22:04:46 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-26 22:07:30 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-26 22:05:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-03-26 22:05:52 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-26 21:01:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-03-26 22:04:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-03-26 22:03:01 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.051 |  |
| 2026-03-26 18:08:43 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.070 |  |
| 2026-03-26 22:03:55 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.097 |  |
| 2026-03-26 21:14:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)