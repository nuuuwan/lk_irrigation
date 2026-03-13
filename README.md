# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_09:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 09:10:34 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-03-13 09:10:21 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.094 |  |
| 2026-03-13 09:09:11 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:08:38 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2026-03-13 09:08:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-03-13 09:07:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:07:12 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:05:58 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.191 |  |
| 2026-03-13 09:05:23 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-03-13 09:04:59 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 09:04:59 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:04:53 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.153 |  |
| 2026-03-13 09:04:43 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-03-13 09:04:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 09:04:19 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:04:05 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:41 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:23 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:13 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 09:03:09 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-13 09:03:09 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:02:41 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.127 |  |
| 2026-03-13 09:02:21 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.051 |  |
| 2026-03-13 09:02:03 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 09:02:00 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:01:57 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:44 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.070 |  |
| 2026-03-13 09:01:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:28 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-13 09:01:10 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.138 |  |
| 2026-03-13 09:01:10 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:00:46 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-03-13 09:00:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 09:03:09 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-13 09:03:13 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 08:12:43 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 09:04:59 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 09:04:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 09:02:03 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 09:02:21 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:57 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:10 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:23 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:09:11 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:09 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:04:19 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:04:05 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:00:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:03:41 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:04:59 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:01:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:07:12 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 09:08:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-03-13 09:10:34 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-03-13 09:02:00 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:07:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:00:46 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-13 09:01:28 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-13 09:08:38 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2026-03-13 09:05:23 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-03-13 09:04:43 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-03-13 09:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-03-13 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.051 |  |
| 2026-03-13 09:01:44 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.070 |  |
| 2026-03-13 09:10:21 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.094 |  |
| 2026-03-13 09:02:41 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.127 |  |
| 2026-03-13 09:01:10 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.138 |  |
| 2026-03-13 09:04:53 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.153 |  |
| 2026-03-13 09:05:58 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)