# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_18:42:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,919 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 18:42:55 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:10:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.018 |  |
| 2026-06-18 18:09:00 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-06-18 18:06:58 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.056 |  |
| 2026-06-18 18:06:35 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-18 18:06:29 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:06:24 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-18 18:06:06 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 18:05:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 18:03:05 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-18 18:04:51 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-18 18:06:35 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-18 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-18 18:00:10 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 18:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 18:02:20 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 18:03:24 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 18:05:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 18:03:02 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 18:02:37 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 18:00:57 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 18:06:06 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:12:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:12 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:57 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:52 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:06:29 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:42:55 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:02:28 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:02:09 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.010 |  |
| 2026-06-18 18:03:51 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-18 18:01:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-06-18 18:02:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-06-18 18:01:14 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-06-18 18:06:24 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-18 18:10:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.018 |  |
| 2026-06-18 18:03:38 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.029 |  |
| 2026-06-18 18:09:00 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-18 18:02:50 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-06-18 18:03:03 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-06-18 18:06:58 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.056 |  |
| 2026-06-18 18:04:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.058 |  |
| 2026-06-18 18:00:57 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)