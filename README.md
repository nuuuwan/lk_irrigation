# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_06:37:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 06:37:34 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-06-20 06:11:53 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-20 06:10:54 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.275 |  |
| 2026-06-20 06:08:32 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-06-20 06:07:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-06-20 06:07:27 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-20 06:06:13 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:06:12 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-06-20 06:06:05 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.044 |  |
| 2026-06-20 06:06:04 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -4.686 |  |
| 2026-06-20 06:05:47 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:04:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:04:18 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:04:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:48 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:03:48 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.104 |  |
| 2026-06-20 06:03:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:34 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.072 |  |
| 2026-06-20 06:03:25 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:24 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-20 06:03:18 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:51 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:02:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:30 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:01:55 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.033 |  |
| 2026-06-20 06:01:50 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 06:06:12 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-06-20 06:07:27 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-20 06:00:14 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-20 06:11:53 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-20 06:00:27 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 06:00:32 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 06:05:47 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:06:13 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:30 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:04:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:00:33 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:00:59 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:18 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:03:25 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:02:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 06:37:34 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-06-20 05:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-06-20 06:07:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-06-20 06:04:18 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:01:50 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:02:51 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 06:03:48 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:03:48 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:04:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-06-20 06:08:32 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-06-20 06:03:24 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-20 06:01:55 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.033 |  |
| 2026-06-20 06:06:05 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.044 |  |
| 2026-06-20 06:00:33 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.056 |  |
| 2026-06-20 06:03:34 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.072 |  |
| 2026-06-20 06:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.104 |  |
| 2026-06-20 06:10:54 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.275 |  |
| 2026-06-20 06:06:04 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -4.686 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)