# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_17:20:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,180 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 17:20:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:17:38 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:12:43 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:11:25 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-10 17:11:11 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.027 |  |
| 2026-05-10 17:10:53 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:10:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-05-10 17:07:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-10 17:07:26 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:07:16 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:06:46 | Katharagama (Menik Ganga) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:06:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:06:27 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.126 |  |
| 2026-05-10 17:06:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:05:55 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.032 |  |
| 2026-05-10 17:05:47 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-10 17:05:47 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:05:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-10 17:04:32 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-05-10 17:04:32 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:03:54 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:03:35 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:03:20 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.056 |  |
| 2026-05-10 17:02:56 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:02:42 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:02:41 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.020 |  |
| 2026-05-10 17:02:28 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-10 17:02:26 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-05-10 17:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:02:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:01:59 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:01:59 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.013 |  |
| 2026-05-10 17:01:51 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:01:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 17:01:43 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:01:19 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:01:14 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:00:53 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:00:29 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 17:05:47 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-10 17:02:28 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-10 17:05:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-10 17:07:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-10 17:01:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 17:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:17:38 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:07:16 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:20:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:12:43 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:10:53 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:06:27 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:02:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:01:59 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:01:19 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:03:35 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:05:47 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-10 17:06:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:06:46 | Katharagama (Menik Ganga) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:06:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-10 17:01:51 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:01:14 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:03:54 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:01:43 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:00:53 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:02:56 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:02:42 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-05-10 17:01:59 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.013 |  |
| 2026-05-10 17:04:32 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-05-10 17:02:41 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.020 |  |
| 2026-05-10 17:11:25 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-10 17:02:26 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-05-10 17:10:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-05-10 17:11:11 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.027 |  |
| 2026-05-10 17:05:55 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.032 |  |
| 2026-05-10 17:00:29 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.042 |  |
| 2026-05-10 17:03:20 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.056 |  |
| 2026-05-10 17:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)