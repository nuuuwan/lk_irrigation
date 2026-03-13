# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_18:10:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 18:10:39 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:09:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:08:49 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:08:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:07:05 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:06:19 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 18:06:00 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-13 18:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:05:17 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 18:04:59 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 18:04:36 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:04:35 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.063 |  |
| 2026-03-13 18:04:34 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:04:24 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 18:04:20 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:04:13 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.043 |  |
| 2026-03-13 18:04:01 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-03-13 18:03:42 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-03-13 18:03:40 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:09 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:03:01 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-13 18:02:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-03-13 18:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:21 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:44 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:42 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:27 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:01:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-03-13 18:01:19 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-13 18:01:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.087 |  |
| 2026-03-13 18:01:11 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-13 18:01:08 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:00:29 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 18:00:29 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:59:45 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 17:20:46 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 18:03:42 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-03-13 18:01:19 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-13 18:04:24 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 18:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-13 18:03:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 17:59:45 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 18:04:59 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 18:00:29 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 18:06:19 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 18:03:01 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-13 18:05:17 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 18:01:27 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:09:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:03:09 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 18:00:29 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:10:39 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:42 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:08:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:08 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:44 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:21 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:07:05 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:40 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:04:34 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:08:49 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:01:11 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-13 18:02:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-03-13 18:06:00 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-13 17:03:12 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.022 |  |
| 2026-03-13 18:04:01 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-03-13 18:04:13 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.043 |  |
| 2026-03-13 18:01:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-03-13 18:04:35 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.063 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-13 18:01:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)