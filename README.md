# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_14:11:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 14:11:20 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:11:18 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:09:37 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-05 14:08:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:07:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-05 14:07:21 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-06-05 14:07:21 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.048 |  |
| 2026-06-05 14:07:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:06:53 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-05 14:06:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:06:13 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-05 14:06:13 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-06-05 14:06:03 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:05:52 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:05:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:05:32 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-06-05 14:05:15 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:05:06 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:04:59 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:04:52 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-05 14:04:32 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 14:07:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-05 14:06:13 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-05 14:04:52 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-05 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-05 14:06:53 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-05 14:05:15 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:06:03 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:05:06 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 14:02:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:00:07 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:05:52 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:05:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:11:20 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:04:59 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:03:29 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:07:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:06:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:08:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:01:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:00:59 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 14:09:37 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-05 14:02:38 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-05 14:06:13 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-06-05 14:07:21 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-06-05 14:03:32 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.015 |  |
| 2026-06-05 14:04:25 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-06-05 14:05:32 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-06-05 14:03:57 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.020 |  |
| 2026-06-05 14:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.020 |  |
| 2026-06-05 14:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-05 14:01:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-06-05 14:03:28 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.032 |  |
| 2026-06-05 14:03:25 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2026-06-05 14:01:58 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.044 |  |
| 2026-06-05 14:07:21 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.048 |  |
| 2026-06-05 14:04:07 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.052 |  |
| 2026-06-05 14:04:32 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.069 |  |
| 2026-06-05 14:04:03 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)