# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_08:38:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 08:38:19 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-13 08:12:43 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 08:10:16 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:07:43 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 08:07:41 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:07:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-13 08:06:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:06:46 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:06:26 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-03-13 08:06:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.156 |  |
| 2026-03-13 08:06:08 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.098 |  |
| 2026-03-13 08:05:53 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-13 08:05:47 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:05:37 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:04:48 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 08:04:34 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-03-13 08:03:48 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 08:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-03-13 08:03:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 08:03:06 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.061 |  |
| 2026-03-13 08:02:56 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:51 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-13 08:02:48 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:43 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:33 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.071 |  |
| 2026-03-13 08:02:32 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.022 |  |
| 2026-03-13 08:02:13 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 08:02:13 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:08 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-13 08:02:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:40 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:01:31 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.041 |  |
| 2026-03-13 08:01:26 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-13 08:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2026-03-13 08:01:23 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:16 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:00:10 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 08:02:08 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-13 08:02:51 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-13 08:05:53 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-13 08:07:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-13 08:01:26 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-13 08:03:48 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 08:12:43 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 08:04:48 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 08:02:13 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 08:07:43 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 08:03:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 08:38:19 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-13 08:02:56 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:16 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:13 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:06:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:10:16 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:40 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:05:37 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:01:23 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:43 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:02:48 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 08:07:41 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:05:47 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:00:10 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:01:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-13 08:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2026-03-13 08:04:34 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-03-13 08:02:32 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.022 |  |
| 2026-03-13 08:01:31 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.041 |  |
| 2026-03-13 08:06:26 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-03-13 08:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-03-13 08:03:06 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.061 |  |
| 2026-03-13 08:02:33 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.071 |  |
| 2026-03-13 08:06:08 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.098 |  |
| 2026-03-13 08:06:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)